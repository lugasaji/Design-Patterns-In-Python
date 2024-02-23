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