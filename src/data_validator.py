class DataValidator:
    
    @staticmethod
    def is_valid_int(input, min=None, max=None):
        '''
        Check whether the user input value is an integer that in the specific range.
        
        Parameters:
        input: user's input.
        min: minimum integer.
        max: maximum integer.
        '''

        # If input is not the instance of int, return false
        if not isinstance(input, int):
            return False
        
        # If input greater than the maximum range, return fales
        if max is not None and input > max:
            return False
        
        # If input lower than the minimum range, return fales
        if min is not None and input < min:
            return False
        
        # Otherwise, return true
        return True