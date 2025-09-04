class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        thousands = num // 1000
        hundreds = num // 100 % 10
        tens = num // 10 % 10
        ones = num % 10
        roman += "M" * thousands
        if hundreds < 4:
            roman += "C" * hundreds
        elif hundreds == 9:
            roman += "CM"
        elif hundreds == 4:
            roman += "CD"
        else:
            roman += "D" + "C" * (hundreds - 5)

        if tens < 4:
            roman += "X" * tens
        elif tens == 9:
            roman += "XC"
        elif tens == 4:
            roman += "XL"
        else:
            roman += "L" + "X" * (tens - 5)

        if ones < 4:
            roman += "I" * ones
        elif ones == 9:
            roman += "IX"
        elif ones == 4:
            roman += "IV"
        else:
            roman += "V" + "I" * (ones - 5)

        return roman