# Basanta Phuyal & Samriddha KC
# CSC 236
# A16: The Animal Game
##################################################################################################

from Tree import BinaryTree

def data_set (node, file):

    '''
    This function sets the categorgy and data of the file
    '''

    file_read = file.readline()                  # variable created
    file_read2 = file.readline()                 # variable created
    node.setData(file_read2)                             # calls the setData function from the BinaryTree class
    if file_read != "Question:\n":
        return
    node.left = BinaryTree()                           # it goes to the left
    data_set(node.left, file)                          # recursive
    node.right = BinaryTree()                          # it goes to the right
    data_set(node.right, file)                         # recursive

def node_creator(ai_guess, user_guess, question):

    '''
    function that creates nodes to the existing tree
    '''

    open_file = open("gamedata.txt", 'r')
    question_list = []
    for i in open_file:                     # for every line it appends to the list
        question_list.append(i)
    if ai_guess in question_list:
        index = question_list.index(ai_guess)
        question_list.insert(index+1, user_guess)
        question_list.insert(index+1, "Guess:\n")
        question_list.insert(index-1, question)
        question_list.insert(index-1, "Question:\n")
    open_again = open("gamedata.txt", 'w')           # opens the txt to write
    for Question in question_list:                  # adds data recieved from user to the file
        open_again.write(Question)
    open_again.close()



def main():
    head = BinaryTree()               # sets the class we imported to head
    open_file = open("gamedata.txt", 'r')         #opens and reads the txt file
    data_set(head, open_file)                         # we call the function from above
    while head.left != None and head.right != None:
        print (head.data)                   # prints the data of head
        user_input = input("Enter Yes or No: ")       # asks for a answer "yes" or "no"
        if user_input.lower() == "yes":            # if yes than it goes to the right
            head = head.right
        elif user_input.lower() == "no":           # if no than it goes to the left
            head = head.left
    print (head.data)
    make_sure = input("Is the guess of the animal correct? ")   # asks user for confirmation
    if make_sure.lower() == "yes":
        print ("GRRAA! I knew it!")
    else:
        TheCorrectAnimal = input("What is the animal that you guessed? ") + "\n"
        question_help = input("Insert a question that whould allow the AI to make a correct guess?: ") + "\n"
        node_creator(head.data, TheCorrectAnimal, question_help)     # calls the function from above
main()




