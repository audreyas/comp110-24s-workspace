def greet(name: str, friendly: bool) -> str: 
    print(f"Hello {name}!")
    if friendly: 
        return f"I'm so happy to see you {name}!"
    else: 
        return "Bye!"
    
def main(): 
    greet("Lizzie", True)



