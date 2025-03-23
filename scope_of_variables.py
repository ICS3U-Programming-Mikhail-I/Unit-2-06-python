#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 23, 2025
# Description: A Python program demonstrating the difference between global and local variables.

# Global variable
global_variable = "I am global"


def main():
    """Main function to demonstrate local and global variable usage."""
    # Local variable
    local_variable = "I am local"

    # Displaying both variables
    print(f"Inside main(): global_variable = {global_variable}")
    print(f"Inside main(): local_variable = {local_variable}")


# Check if this script is being run directly and call the main function
if __name__ == "__main__":
    main()
