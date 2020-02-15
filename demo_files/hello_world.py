#/usr/bin/python3

'''Example .py script to be run from the command line.'''


def hello_world(text):
	print(f"This is just a note to say: {text}!")


def main():
	say_hello = "hello world"
	hello_world(say_hello)


if __name__ == "__main__":
	main()