def log_and_run(func):
  print(f"I just got {func.__name__}")
  return func()


def log_and_return(func):
  print(f"I just got {func.__name__}")
  return func


def say_hello():
  print('Hello!')


print("log and run:")
log_and_run(say_hello)

print("log and return:")
hola = log_and_return(say_hello)
hola()
