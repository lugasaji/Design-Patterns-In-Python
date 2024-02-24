from abc import abstractmethod


class Machine:
    def print(self, document) -> NotImplementedError:
        raise NotImplementedError
    
    def fax(self, document) -> NotImplementedError:
        raise NotImplementedError
    
    def scan(self, document) -> NotImplementedError:
        raise NotImplementedError
    

class MultiFunctionPrinter(Machine):
    def print(self, document) -> NotImplementedError:
        pass

    def fax(self, document) -> NotImplementedError:
        pass

    def scan(self, document) -> NotImplementedError:
        pass


class OldFashionedPrinter(Machine):
    def print(self, document) -> NotImplementedError:
        pass

    def fax(self, document) -> NotImplementedError:
        pass # Don't supported

    def scan(self, document) -> NotImplementedError:
        pass # Don't supported


# Soluction to violation ISP
    
class Printer:

    @abstractmethod
    def print(self, document):
        pass

class Scanner:

    @abstractmethod
    def scan(self, document):
        pass

class Fax:

    @abstractmethod
    def fax(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def scan(self, document):
        pass

class NewMultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass


 
class MultiFunctionDevice(Printer, Scanner):
    
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, scanner: Scanner ) -> None:
        self.printer = printer
        self.scanner = scanner
    
    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)