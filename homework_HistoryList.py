class PageNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class HistoryList:
    def __init__(self):
        self.head = None  
        self.tail = None  
        self.current = None  
        
    def add_page(self, url):
       
        new_node = PageNode(url)
        
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.current = new_node  
    
    def go_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.url
        return None
    
    def go_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.url
        return None
    
    def remove_last_page(self):
        if self.tail is None: 
            return
        
        if self.head == self.tail: 
            self.head = None
            self.tail = None
            self.current = None
        else:
            if self.current == self.tail:
                self.current = self.tail.prev
                
            self.tail = self.tail.prev
            self.tail.next = None
    
    def print_current(self):
        if self.current:
            print(f"Текущая страница: {self.current.url}")
        else:
            print("История пуста")
    
    def print_history(self):
        if self.head is None:
            print("История пуста")
            return
        
        print("Вся история посещений:")
        current = self.head
        while current:
            prefix = "-> " if current == self.current else "   "
            print(f"{prefix}{current.url}")
            current = current.next

if __name__ == "__main__":
    history = HistoryList()
    
    pages = ["google.com", "youtube.com", "github.com", "python.org", "stackoverflow.com"]
    for page in pages:
        history.add_page(page)
    
    print("После добавления страниц:")
    history.print_current()
    history.print_history()
    
    print("\nПеремещаемся на 2 страницы назад:")
    history.go_back()
    history.go_back()
    history.print_current()
    
    print("\nПеремещаемся на 1 страницу вперед:")
    history.go_forward()
    history.print_current()
    
    print("\nУдаляем последнюю страницу из истории:")
    history.remove_last_page()
    history.print_current()
    history.print_history()