def minimize_ticket_price(ticket_price: str, k: int) -> str:
    stack = []
    remaining_removals = k
    for digit in ticket_price:
        while stack and remaining_removals > 0 and stack[-1] > digit:
            stack.pop()
            remaining_removals -= 1
        stack.append(digit)
    final_stack = stack[:len(stack) - remaining_removals]

    result = ''.join(final_stack).lstrip('0')

    return result if result else "0"

ticket_price = input("Enter the ticket price: ")
k = int(input("Enter the number of digits to remove: "))

print(minimize_ticket_price(ticket_price, k))
