def accumulate_data(data_size):
  data = []
  for i in range(data_size):
    data.append(i * i)  # Simulate some data generation
  return data

@profile
def bob():
  # Call the function repeatedly to leak memory
  for _ in range(10):
    accumulate_data(100)

def main():
    bob()
    print("im done here")
    print("hi there we are about to exit")

if __name__ == "__main__":
  main()
