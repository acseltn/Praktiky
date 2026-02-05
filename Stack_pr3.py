# ЗАДАНИЕ 1: MaxStack 

print("1.")
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def push(self, x):
        self.stack.append(x)
        # В max_stack всегда лежит текущий максимум
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])  # максимум не изменился
    
    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()
    
    def get_max(self):
        return self.max_stack[-1]


s = MaxStack()
s.push(5)
s.push(3)
s.push(10)
s.push(2)

print(f"Стек: {s.stack}")
print(f"Максимум: {s.get_max()}")  # 10
s.pop()
print(f"После удаления 2: максимум = {s.get_max()}")  # 10
s.pop()
print(f"После удаления 10: максимум = {s.get_max()}")  # 5
print()

# ЗАДАНИЕ 2: ПРОСТОЙ КАЛЬКУЛЯТОР 
print("2.")
def simple_calculator(expr):
    """Самый простой калькулятор (без скобок и степеней)"""
    # Убираем пробелы и разбиваем
    expr = expr.replace(' ', '')
    
    # Преобразуем "-5" в "0-5" для унарного минуса
    if expr.startswith('-'):
        expr = '0' + expr
    
    result = 0
    current_num = ''
    last_operator = '+'
    
    for i, char in enumerate(expr):
        if char.isdigit() or char == '.':
            current_num += char
        else:
            # Когда встречаем оператор, обрабатываем предыдущее число
            num = float(current_num) if current_num else 0
            
            if last_operator == '+':
                result += num
            elif last_operator == '-':
                result -= num
            elif last_operator == '*':
                result *= num
            elif last_operator == '/':
                result /= num
            
            last_operator = char
            current_num = ''
    
    # Обрабатываем последнее число
    if current_num:
        num = float(current_num)
        if last_operator == '+':
            result += num
        elif last_operator == '-':
            result -= num
        elif last_operator == '*':
            result *= num
        elif last_operator == '/':
            result /= num
    
    return result

# Тестируем
expressions = ["2+3*4", "10/2", "3.5*2"]
for expr in expressions:
    print(f"{expr} = {simple_calculator(expr)}")

# ЗАДАНИЕ 3: ПРОСТОЙ СИМУЛЯТОР ПРОЦЕССОРА 
print("3.")
print("Доступные команды:")
print("  PUSH <число>  - положить число на стек")
print("  POP           - удалить верхний элемент")
print("  ADD           - сложить два верхних числа")
print("  SUB           - вычесть (верхнее из нижнего)")
print("  MUL           - умножить")
print("  DIV           - разделить")
print("  DUP           - дублировать верхний элемент")
print("  SWAP          - поменять местами два верхних")
print("  SHOW          - показать текущий стек")
print("  EXIT          - завершить программу")
print("=" * 50)

class InteractiveCPU:
    def __init__(self):
        self.stack = []
    
    def show_stack(self):
        """Показать стек в красивом виде"""
        if not self.stack:
            print("  [СТЕК ПУСТ]")
        else:
            print("  Стек (сверху вниз):")
            for i, value in enumerate(reversed(self.stack), 1):
                print(f"    {i}. {value}")
    
    def run_interactive(self):
        """Запуск интерактивного режима"""
        print("\n💻 Начинаем работу! Введите команды:")
        
        while True:
            # Показываем текущий стек
            print("\n" + "-" * 30)
            self.show_stack()
            print("-" * 30)
            
            # Получаем команду от пользователя
            command = input(">>> ").strip().upper()
            
            if command == "EXIT":
                print("👋 Программа завершена!")
                break
            
            elif command == "SHOW":
                continue  # стек уже показан выше
            
            elif command.startswith("PUSH"):
                # Извлекаем число из команды
                parts = command.split()
                if len(parts) != 2:
                    print("❌ Ошибка: PUSH требует число. Пример: PUSH 5")
                    continue
                
                try:
                    number = float(parts[1])
                    self.stack.append(number)
                    print(f"✅ Положили {number} на стек")
                except ValueError:
                    print("❌ Ошибка: это не число!")
            
            elif command == "POP":
                if not self.stack:
                    print("❌ Ошибка: стек пуст!")
                else:
                    removed = self.stack.pop()
                    print(f"✅ Удалили {removed} с вершины стека")
            
            elif command in ["ADD", "SUB", "MUL", "DIV"]:
                if len(self.stack) < 2:
                    print(f"❌ Ошибка: нужно минимум 2 числа для {command}")
                    continue
                
                # Берём два верхних числа
                b = self.stack.pop()
                a = self.stack.pop()
                
                if command == "ADD":
                    result = a + b
                    print(f"✅ {a} + {b} = {result}")
                elif command == "SUB":
                    result = a - b
                    print(f"✅ {a} - {b} = {result}")
                elif command == "MUL":
                    result = a * b
                    print(f"✅ {a} * {b} = {result}")
                elif command == "DIV":
                    if b == 0:
                        print("❌ Ошибка: деление на ноль!")
                        # Возвращаем числа обратно
                        self.stack.append(a)
                        self.stack.append(b)
                        continue
                    result = a / b
                    print(f"✅ {a} / {b} = {result}")
                
                self.stack.append(result)
            
            elif command == "DUP":
                if not self.stack:
                    print("❌ Ошибка: стек пуст!")
                else:
                    top = self.stack[-1]
                    self.stack.append(top)
                    print(f"✅ Дублировали {top}")
            
            elif command == "SWAP":
                if len(self.stack) < 2:
                    print("❌ Ошибка: нужно минимум 2 числа для SWAP")
                else:
                    self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
                    print(f"✅ Поменяли местами {self.stack[-1]} и {self.stack[-2]}")
            
            else:
                print("❌ Неизвестная команда! Введите HELP для списка команд")
                if command == "HELP":
                    print("Доступные команды: PUSH, POP, ADD, SUB, MUL, DIV, DUP, SWAP, SHOW, EXIT")

# Запускаем процессор
cpu = InteractiveCPU()
cpu.run_interactive()