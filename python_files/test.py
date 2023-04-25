import torch
import torch.nn.functional as F
from torch.distributions import Categorical
import numpy as np
from train import RNN
import sys

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def test():
    ############ Hyperparameters ############
    hidden_size = 512   # size of hidden state
    num_layers = 3      # num of layers in LSTM layer stack
    op_seq_len = 1000   # total num of characters in output test sequence
    
    if sys.argv[1] == "Turkish":
        load_path = "./preTrained/Turkish-Kenet.pth"
        train_data_path = "./UD_Turkish-Kenet/tr_words_train_filtered_shuf.txt"
        test_data_path = "./UD_Turkish-Kenet/tr_words_test_filtered_shuf.txt"
    elif sys.argv[1] == "Finnish":
        load_path = "./preTrained/Finnish-PUD.pth"
        train_data_path = "./UD_Finnish-PUD/fi_words_train_filtered_shuf.txt"
        test_data_path = "./UD_Finnish-PUD/fi_words_test_filtered_shuf.txt"
    elif sys.argv[1] == "Chukchi":
        load_path = "./preTrained/Chukchi-HSE.pth"
        train_data_path = "./UD_Chukchi-HSE/ckt_words_train_filtered_shuf.txt"
        test_data_path = "./UD_Chukchi-HSE/ckt_words_test_filtered_shuf.txt"

    #########################################
    
    # load the text file
    train_data = open(train_data_path, 'r').read()
    test_data = open(test_data_path, 'r').read()

    # Set chars equal to larger value between unique chars in data in train v test
    chars = sorted(list(set(train_data).union(set(test_data))))

    data_size, vocab_size = len(test_data), len(chars)
    print("----------------------------------------")
    print(f"Data path: {test_data_path}")
    print(f"Data has {data_size} characters, {vocab_size} unique")
    print("----------------------------------------")
    
    # char to index and idex to char maps
    char_to_ix = { ch:i for i,ch in enumerate(chars) }
    ix_to_char = { i:ch for i,ch in enumerate(chars) }
    
    # convert data from chars to indices
    data = list(test_data)
    for i, ch in enumerate(data):
        data[i] = char_to_ix[ch]
    
    # data tensor on device
    data = torch.tensor(data).to(device)
    data = torch.unsqueeze(data, dim=1)
    
    # create and load model instance
    rnn = RNN(vocab_size, vocab_size, hidden_size, num_layers).to(device)
    rnn.load_state_dict(torch.load(load_path))
    print("Model loaded successfully !!")
    
    # initialize variables
    data_ptr = 0
    hidden_state = None
    
    # randomly select an initial string from the data
    rand_index = np.random.randint(data_size - 11)
    input_seq = data[rand_index : rand_index + 9]
    
    # compute last hidden state of the sequence 
    _, hidden_state = rnn(input_seq, hidden_state)
    
    # next element is the input to rnn
    input_seq = data[rand_index + 9 : rand_index + 10]
    
    # generate remaining sequence
    print("----------------------------------------")
    while True:
        # forward pass
        output, hidden_state = rnn(input_seq, hidden_state)
        
        # construct categorical distribution and sample a character
        output = F.softmax(torch.squeeze(output), dim=0)
        dist = Categorical(output)
        index = dist.sample().item()
        
        # print the sampled character
        print(ix_to_char[index], end='')
        
        # next input is current output
        input_seq[0][0] = index
        data_ptr += 1
        
        if data_ptr  > op_seq_len:
            break
        
    print("\n----------------------------------------")
   
if __name__ == '__main__':
    test()
