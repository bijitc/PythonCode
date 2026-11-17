
MemberName = input("Enter member name: ")
ClubName = input("Enter club name: ")


member_number = 7
points = 9.5
is_active = True

print(f"Member Number: {member_number} (Type: {type(member_number)})")
print(f"Points: {points} (Type: {type(points)})")
print(f"Is Active: {is_active} (Type: {type(is_active)})")

badge_code = MemberName[:3] + ClubName[-1] + str(member_number)
print(f"Badge Code: {badge_code}")


print("===== CLUB BADGE =====")
print("Member: " + MemberName)
print("Club: " + ClubName)
print("Code: " + badge_code)
print("Points | Active: " + str(points) + " | " + str(is_active))
print("========================")