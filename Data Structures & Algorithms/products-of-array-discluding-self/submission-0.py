class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        zero_count = nums.count(0)
        output = [1] * length
        # Validamos si hay mas de 2 ceros
        if zero_count > 1:
            return [0] * length
        # Validamos si hay un cero y la posicion del mismo. 
        elif zero_count == 1:
            zero_index = nums.index(0)
            total_product = 1

            for i in range(length):
                if i != zero_index:
                    total_product *= nums[i]

            output = [0] * length
            output[zero_index] = total_product

            return output

        else:
            # Producto de los elementos de la izquierda
            left_product = 1

            for i in range(length):
                output[i] = left_product
                left_product *= nums[i]

            # Producto de los elementos de la derecha
            right_product = 1

            for i in range(length - 1, -1, -1):
                output[i] *= right_product
                right_product *= nums[i]

            return output
        