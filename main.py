class Stos:
    def __init__(self, length):
        self.top= 0
        self.stos= [0]* length
        self.n= length

    def push(self, a):
        self.top+= 1
        self.stos[self.top- 1]= a

    def pop(self):
        if self.top== 0:
            print("stos jest pusty")
        else:
            a= self.stos[self.top- 1]
            self.stos[self.top- 1]= 0
            self.top-= 1
            return a

    def find(self, a):
        for i in range (self.n):
            if a == self.stos[i]:
                return i


class Kolejka:

    def __init__(self, length):
        self.kolejka= [0]* length
        self.head= 0
        self.tail= 0
        self.n= length

    def dequeue(self):
        if self.head!= self.tail:
            a= self.kolejka[self.head]
            self.kolejka[self.head]= 0
            if self.head< self.n- 1:
                self.head+= 1
            else:
                self.head= 0
            return a
        else:
            print("kolejka jest pusta")

    def enqueue(self, a):
        if self.tail< (self.n- 1):
            if self.head!= self.tail+ 1:
                self.kolejka[self.tail]= a
                self.tail+= 1
            else:
                print("kolejka jest pelna")
        else:
            if self.head!= 0:
                self.kolejka[self.tail]= a
                self.tail= 0
            else:
                print("kolejka jest pelna")

    def find(self, a):
        if self.tail> self.head:
            for i in range(self.head, self.tail):
                if self.kolejka[i] == a:
                    return i
        else:
            for i in range(0, self.n)):
                if self.tail<= i< self.head:
                    continue
                if self.kolejka[i]> a:
                    return i


class KolejkaPriorytetowa:

    def __init__(self, length):
        self.kolejkaPR= [0]* length
        self.head= 0
        self.tail= 0
        self.n= length

    def enqueue(self, a):
        if self.tail< (self.n- 1):
            if self.head!= self.tail+ 1:
                self.kolejkaPR[self.tail]= a
                self.tail+= 1
            else:
                print("kolejka jest pelna")
        else:
            if self.head!= 0:
                self.kolejkaPR[self.tail]= a
                self.tail= 0
            else:
                print("kolejka jest pelna")

    def dequeue(self):
        max=self.kolejkaPR[0]
        index_max= 0
        for i in range (0, self.n):
            if self.kolejkaPR[i]> max:
                max= self.kolejkaPR[i]
                index_max= i
        self.kolejkaPR[self.head], self.kolejkaPR[index_max]= self.kolejkaPR[index_max], self.kolejkaPR[self.head]

        if self.head!= self.tail:
            a= self.kolejkaPR[self.head]
            self.kolejkaPR[self.head]= 0
            if self.head<self.n- 1:
                self.head+= 1
            else:
                self.head= 0
            return a
        else:
            print("kolejka jest pusta")

    def find(self, a):
        if self.tail> self.head:
            for i in range(self.head, self.tail):
                if self.kolejkaPR[i] == a:
                    return i
        else:
            for i in range(0, self.n):
                if self.tail<= i< self.head:
                    continue
                if self.kolejkaPR[i]> a:
                    return i


class ListaJednokierunkowa:
    class Cell:
        def __init__(self, a):
            self.value= a
            self.next= None

    def __init__(self):
        self.head= self.Cell("head")

    def getLastCell(self, head):
        cell= head
        if cell.next is None:
            return cell
        lastcell= cell.next
        return self.getLastCell(lastcell)

    def getCellIndex(self, index):
        if index< 0:
            return None
        cell= self.head.next
        i= 0
        if cell is None:
            return None
        while i< index:
            if cell.next is None:
                return None
            cell= cell.next
            i+= 1
        return cell

    def addLastCell(self, a):
        newcell= self.Cell(a)
        lastcell= self.getLastCell(self.head)
        lastcell.next= newcell

    def add(self, a, index):
        if index< 0:
            return None
        newcell= self.Cell(a)
        newcell.next= self.getCellIndex(a)
        previouscell= self.getCellIndex(a- 1)
        if previouscell is None and index== 0:
            self.head.next = newcell
            return
        elif previouscell is None:
            print("blad, zbyt duzy indeks")
            return
        previouscell.next= newcell

    def remove(self, index):
        if index< 0:
            return None
        cell= self.getCellIndex(index)
        if index!= 0 and self.getCellIndex(index) is None:
            print("blad, zbyt duzy indeks")
            return
        elif index== 0 and cell.next is None:
            self.head.next= None
            return
        elif index== 0:
            self.head.next= cell.next
            return
        elif cell.next is None:
            self.getCellIndex(index- 1).next = None
            return
        self.getCellIndex(index- 1).next= self.getCellIndex(index+ 1)

    def find(self, a):
        i= 0
        cell= self.head
        while true:
            if cell.a== a:
                return i
            cell= cell.next
            if cell is None:
                return None
            i+= 1

class ListaDwukierunkowa:

      def append(self, a):
        cell= Cell(a)
        if self.head is None:
            self.tail= cell
            self.head= cell
            self.head.previous= self.tail
            self.tail.next= self.head
        else:
            cell.previous= self.tail
            cell.previous.next= cell
            self.tail= cell

class Lista_z_Wartownikiem:

    def __init__(self):
        self.head = None
        self.tail = None
        self.guard = Cell(None)
        self.guard.next = self.head
        self.guard.previous = self.tail

    def append(self, a):
        cell = Cell(a)
        cell = Cell(a)
        if self.head is None:
            self.head = cell
            self.tail = cell
            self.head.previous = self.tail
            self.tail.next = self.head
            self.guard.previous = self.tail
            self.guard.next = self.head
        else:
            cell.previous = self.tail
            cell.previous.next = cell
            self.tail = cell
            self.guard.previous = self.tail

    def insert(self, a, index= 0):
        cell = self.head
        if index<0:
            print('zly indeks')
        elif index == 0:
            cell = Cell(a)
            cell.next = self.head
            self.head = cell
            self.guard.next = self.head
        else:
            for i in range(index):
                if i+1==index:
                    cl = Cell(a)
                    cl.next = cell.next
                    cl.previous = cell
                    cell.next = cl
                cell = cell.next

    def remove(self, index):
        cell= self.head
        if index == 0:
            self.head= self.head.next
            self.guard.next= self.head
        else:
            for i in range(index+ 1):
                if i==index:
                    if cell==self.head:
                        self.head= cell.next
                        self.guard.next= cell.next
                        cell.next.previous= cell.previous
                        cell.previous= None

                    elif cell== self.tail:
                        self.tail= cell.previous
                        self.guard.previous= cell.previous
                        cell.next= None
                        cell.previous.next= cell.next
                    else:
                        cell.next.previous= cell.previous
                        cell.previous.next= cell.next
                cell= cell.next

    def find(self, q):
        self.guard.a= q
        cell= self.head
        index= 0
        while cell is not None:
            if cell.a == self.guard.a:
                return index
            index+= 1
            cell= cell.next
