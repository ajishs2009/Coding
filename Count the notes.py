total = int(input("The total amount is: "))
note_1 = total//100
note_2 = total%100//50
note_3 = (total%100)%50//10
note_4 = (((total%100)%50)%10)//20
print("No. of 100Rs notes are:", note_1)
print("No. of 50Rs notes are:", note_2)
print("No. of 10 Rs notes are:", note_3)
print("No. of 20Rs notes are", note_4)