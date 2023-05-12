def log_and_run(func):
  print(f"I just got {func.__name__}")
  return func()


def log_and_return(func):
  print(f"I just got {func.__name__}")
  return func
