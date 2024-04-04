import difflib

class DiffUpdate:

    def __init__(self):
        pass

    def update(self, changes, direction = 2):
        
        new_content = list(difflib.restore(changes, direction))
        return new_content
    
# lvcs_updater = DiffUpdate()
# content = lvcs_updater.update(
#     changes = ''' \n def factorial(n):\n     if n == 0:\n+        # base case \n         return 1\n     else:\n-        print(\"recursion\")\n-        print(\"Exclamation\")\n         return n * factorial(n - 1)\n \n # Example usage:'''
# )

# print(content)