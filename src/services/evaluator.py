from collections import deque


class Evaluator:
    """Luokka, joka laskee matemaattisen lausekkeen postfix notaatiomuodossa ja palauttaa vastauksen
    """

    def evaluate(self, postfix):
        """Metodi, joka laskee potfix muotoisen lausekkeen arvon.

        Argumentit:
            postfix (lista): Ottaa listana postfix muodossa olevan lausekkeen.
                            Muutta tämän deque -jonoksi.
        Returns:
            int/float: Palauttaa lausekkeen arvon.
        """

        stack = []
        queue = deque(postfix)

        while len(queue) > 0:
            token = queue.popleft()
            if isinstance(token, (int, float)):
                stack.append(token)
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                match token:
                    case "+":
                        stack.append(first_operand + second_operand)
                    case "-":
                        stack.append(first_operand - second_operand)
                    case "*":
                        stack.append(first_operand * second_operand)
                    case "^":
                        stack.append(first_operand ** second_operand)
                    case "/":
                        try:
                            result = first_operand / second_operand
                            stack.append(result)
                        except ZeroDivisionError:
                            return "Virhe: Nollalla jako"

        return stack.pop()
