from random import SystemRandom
import random, time, string

MSG_move_cursor = '''Move your mouse for a few seconds to ensure randomness.
Press enter when done.'''

NUM_SEEDS = 20

def prompt_user_for_randomness():
    raw_input(MSG_move_cursor)

def generate_seed():
    seed_length = 81
    valid_chars = string.ascii_uppercase + '9'
    
    def generate_entropy_rn():
        sysrng = SystemRandom()
        return ''.join([sysrng.choice(valid_chars) for i in range(seed_length)])

    def generate_timestamp_rn(entropy_rn):
        current_time = time.time()
        random.seed(current_time)
        timestamp_rn = []
        for i in range(seed_length):
            timestamp_random_char = random.choice(valid_chars)
            chars = (timestamp_random_char, entropy_rn[i])
            timestamp_rn.append(random.choice(chars))
        assert(len(timestamp_rn) == 81)
        return ''.join(timestamp_rn)

    entropy_rn = generate_entropy_rn()
    return generate_timestamp_rn(entropy_rn)

def main():
    prompt_user_for_randomness()
   
    for i in range(NUM_SEEDS):
        print 'Seed #%d'%(i+1)
        print generate_seed()

main()
