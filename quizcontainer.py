import random

# quiz introduction
print("🌟 Welcome to Python CS 135 Quiz! 🌟\
\n\n📝 This test contains 12 randomized questions about Racket (intermediate with lambda).\
\n📚 Question types include multiple choice, true/false, and short answer.\
\n🔁 Retake it more than once to practise with new sets of questions!\n")
name = input("💻 Please type in your name: ")
print("\n👋 Hi, " + name + "!")
input("👀 Hit ENTER to start: ")


# define class for prompt/answer pairs
class Question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# create lists of question prompts
# create lists of prompt/answer questions

# multiple choice (mc) prompts
mc_prompts = [
    "\nMultiple Choice: Define 'the generalization of similar expressions'.\
\n a) Functions \n b) Equations \n c) Values \n d) None of the above \nAnswer: ",

    "\nMultiple Choice: What is an example of a value?\
\n a) Numbers \n b) Lists \n c) Functions \n d) All of the above \nAnswer: ",

    "\nMultiple Choice: In what type of recursion can an argument be a partial answer?\
\n a) Simple \n b) Generative \n c) Accumulative \n d) Mutual \nAnswer: ",

    "\nMultiple Choice: Why do we use locals?\
\n a) Efficiency \n b) Encapsulation \n c) Clarity \n d) All of the above \nAnswer: ",

    "\nMultiple Choice: What is make-posn?\
\n a) Coordinate \n b) Constructor \n c) Selector \n d) Field \nAnswer: ",

    "\nMultiple Choice: Which of these is a type predicate?\
\n a) make-posn \n b) posn-x \n c) posn? \n d) def-posn\nAnswer: ",

    "\nMultiple Choice: Which statement(s) is correct about foldr and foldl?\
\n a) foldr and foldr produce the same results\
\n b) foldl generalizes accumulative recursion\
\n c) All of the above \n d) None of the above \nAnswer: ",

    "\nMultiple Choice: Who wrote articles describing the operations of the Analytical Engine?\
\n a) Ada Augusta Byron \n b) Charles Babbage \n c) David Hilbert \n d) Alan Turing \nAnswer: "
]

# multiple choice (mc) questions
mc_questions = [
    Question(mc_prompts[0], "a"),
    Question(mc_prompts[1], "d"),
    Question(mc_prompts[2], "c"),
    Question(mc_prompts[3], "d"),
    Question(mc_prompts[4], "b"),
    Question(mc_prompts[5], "c"),
    Question(mc_prompts[6], "b"),
    Question(mc_prompts[7], "a")
]

# true/false (tf) prompts
tf_prompts = [
    "\nTrue (T) or False (F): Expressions combine values with operators and functions.\nAnswer: ",
    "\nTrue (T) or False (F): (or false (string=? “A” “AA”)) produces false.\nAnswer: ",
    "\nTrue (T) or False (F): Helpers used to define constants can be defined after being used.\nAnswer: ",
    "\nTrue (T) or False (F): (cons 1 (cons 2 (cons 3 empty) empty)) and (list 1 2 3) are the same value.\nAnswer: ",
    "\nTrue (T) or False (F): An association list is a list of (key, value) pairs.\nAnswer: ",
    "\nTrue (T) or False (F): The Euclidean algorithm employs mutual recursion.\nAnswer: ",
    "\nTrue (T) or False (F): In a Binary Tree, each node has exactly 2 children.\nAnswer: ",
    "\nTrue (T) or False (F): Functions can be consumed, produced, or both.\nAnswer: "
]

# true/false (tf) questions
tf_questions = [
    Question(tf_prompts[0], "T"),
    Question(tf_prompts[1], "T"),
    Question(tf_prompts[2], "F"),
    Question(tf_prompts[3], "F"),
    Question(tf_prompts[4], "T"),
    Question(tf_prompts[5], "F"),
    Question(tf_prompts[6], "F"),
    Question(tf_prompts[7], "T")
]

# short answer (short) prompts
short_prompts = [
    "\nShort Answer: What will (and (< 1 0) (/ 1 0)) produce?\nAnswer: ",
    "\nShort Answer: What comes after examples in the design recipe?\n",
    "\nShort Answer: In one word, what type of recursion arises when two functions apply each other?\n",
    "\nShort Answer: How many selector functions does Posn have? Enter a number.\n",
    "\nShort Answer: What do we call a set of nodes and edges where an edge connects two distinct nodes?\n",
    "\nShort Answer: In one word, what do we call the process of finding similarities or common aspects, \
and forgetting unimportant differences?\n",
    "\nShort Answer: In one word, which higher order function always consumes a function and a list(s), \
and produces a list?\n",
    "\nShort Answer: Enter the full name of the person who invented Lisp, a LISt Processor.\n"
]

# short answer (short) questions
short_questions = [
    Question(short_prompts[0], "false"),
    Question(short_prompts[1], "contract"),
    Question(short_prompts[2], "mutual"),
    Question(short_prompts[3], "2"),
    Question(short_prompts[4], "tree"),
    Question(short_prompts[5], "abstraction"),
    Question(short_prompts[6], "filter"),
    Question(short_prompts[7], "john mccarthy")
]

# create list of random questions, 4 of each question type
random_questions = random.sample(mc_questions, 4)
random_tf = random.sample(tf_questions, 4)
random_short = random.sample(short_questions, 4)

random_questions.extend(random_tf)
random_questions.extend(random_short)


# function to run quiz on a list of questions, produce score
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer.lower():
            score += 1
    print("\n✏️ You got " + str(score) + "/" + str(len(questions)) + " correct. \
Thank you for participating, " + name + "!")


# quiz function call
run_quiz(random_questions)
