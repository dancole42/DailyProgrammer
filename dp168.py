	from random import choice, randint

	class Language(object):
	    """A language with a defined letters and syllable patterns."""

	    def __init__(self, name, c, v, p, pattern):

	        w = c + v + p # Creates wildcards.
	        word_sizes = {1:100, 2:50, 3:10, 4:5, 5:1} # Word size frequencies
	        self.name = name
	        self.letters = {'c': c, 'v': v, 'w': w, 'p': p}
	        self.pattern = pattern
	        self.syllable_freq = [int(x) for x in (''.join([str(freq)*word_sizes[freq] for freq in word_sizes]))]

	    def get_syllable(self):
	        """Creates a single syllable in the language."""

	        return ''.join([choice(self.letters[letter]) for letter in choice(self.pattern)])

	    def get_word(self, size='default', word=''):
	        """Creates a single word in the language."""

	        if size == 'default':
	            size = choice(self.syllable_freq)
	        while size > 0:
	            size -= 1
	            word += ''.join([syllable for syllable in self.get_syllable()])
	        return word

	def print_class(language, class_size=10):
	    """Prints two ProperCase words (i.e. names) and five random test scores."""
	    header = '\n'+ language.name + " Students"
	    print header
	    print '-' * len(header)
	    for student in range(class_size):
	        print ', '.join([language.get_word().capitalize() for name in range(2)]),
	        print ' '.join([str(randint(0,100)) for x in range(5)])

	# First, set consonants, vowels, and syllable patterns for the language.
	# Syllable patterns must use c (consonant), v (vowel), or w (wildcard).
	# Create as many syllable patterns as you want.
	consonants = ['p', 'v', 't', 'r', 'd', 'd']
	vowels = ['e', 'o', 'u']
	phonograms = ['up', 'down', 'vot']
	patterns = ('cv', 'vc', 'pv', 'ww')
	redditorian = Language("Redditorian", consonants, vowels, phonograms, patterns) # Create the language.
	class_size = 10

	consonants = ['m', 'n', 'p', 't', 'd', 'k', 'g', 's', 'z', 'j', 'w', 'r']
	vowels = ['a', 'i', 'e', 'i', 'u']
	phonograms = []
	patterns = ('vv', 'cv', 'cwv')
	asian_ish = Language("Asian...ish", consonants, vowels, phonograms, patterns) # Create the language.
	class_size = 10

	print_class(redditorian)
	print_class(asian_ish)