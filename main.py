from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet()
    
    # Test initial status
    print("Initial status:")
    my_pet.get_status()
    
    # Test eating
    print("\nTesting eating:")
    my_pet.eat()
    my_pet.get_status()
    
    # Test playing
    print("\nTesting playing:")
    my_pet.play()
    my_pet.get_status()
    
    # Test sleeping
    print("\nTesting sleeping:")
    my_pet.sleep()
    my_pet.get_status()
    
    # Test training and tricks
    print("\nTesting tricks:")
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.show_tricks()
    
    # Test training the same trick twice
    print("\nTesting duplicate trick:")
    my_pet.train("sit")
    
    # Final status check
    print("\nFinal status:")
    my_pet.get_status()

if __name__ == "__main__":
    main()
