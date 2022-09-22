#Autor: Lir Goffer, ID:209103274

class TreeError(Exception):
    """
    tree error class
    """
    def __init__(self, entry):
        super().__init__(entry)


class TreeIllegalValue(TreeError):
    """
    illegal value to remove class
    """
    def __init__(self, entry):
        msg = f"attempted to remove a value ({entry}) that's not in a leaf"
        super().__init__(msg)


class TreeValueDoesNotExist(TreeError):
    """
    not exist value to remove class
    """
    def __init__(self, entry):
        msg = f"attempted to remove a value ({entry}) that doesn't exist"
        super().__init__(msg)


class NaryTree:
    """
    tree data structure class
    """
    def __init__(self, entry):
        self.entry = entry
        self.children = [None, None, None, None]

    def __str__(self):
        """
        str represent of class
        :return: string
        """
        s = f"{self.entry}"
        if self.children:
            s += "["
            for child in self.children[:-1]:
                if child:
                    s += f"{str(child)};"
            if self.children[-1]:
                s += f"{str(self.children[-1])}"
            s += "]"
        return s

    def __repr__(self):
        return (str(self))

    def addEntry(self, entry):
        """
        add value to tree
        :param entry: value
        :return: none
        """
        if entry <= self.entry:
            if not self.children[0]:
                self.children[0] = NaryTree(entry)
            else:
                if not self.children[1]:
                    if self.children[0].entry < entry:
                        self.children[1] = NaryTree(entry)
                    else:
                        self.children[1] = self.children[0]
                        self.children[0] = NaryTree(entry)
                else:
                    if entry <= self.children[0].entry:
                        self.children[0].addEntry(entry)
                    else:
                        self.children[1].addEntry(entry)
        else:
            if not self.children[2]:
                self.children[2] = NaryTree(entry)
            else:
                if not self.children[3]:
                    if self.children[2].entry < entry:
                        self.children[3] = NaryTree(entry)
                    else:
                        self.children[3] = self.children[0]
                        self.children[2] = NaryTree(entry)
                else:
                    if entry <= self.children[2].entry:
                        self.children[2].addEntry(entry)
                    else:
                        self.children[3].addEntry(entry)

    def removeEntry(self, entry):
        """
        remove value from tree
        :param entry: value
        :return: none
        """
        if self.children == [None, None, None, None] and self.entry != entry:
            raise TreeValueDoesNotExist(entry)
        if self.entry == entry and self.children != [None, None, None, None]:
            raise TreeIllegalValue(entry)
        entry_list = []
        for ch in self.children:
            if ch:
                entry_list.append(ch.entry)
            else:
                entry_list.append(None)
        if entry in entry_list:
            i = entry_list.index(entry)
            child = self.children[i]
            if child.children != [None, None, None, None]:
                raise TreeIllegalValue(entry)
            else:
                self.children[i] = None
        else:
            if entry <= self.entry:
                if self.children[0]:
                    if entry <= self.children[0].entry:
                        self.children[0].removeEntry(entry)
                    else:
                        if self.children[1]:
                            self.children[1].removeEntry(entry)
                        else:
                            raise TreeValueDoesNotExist(entry)
                else:
                    raise TreeValueDoesNotExist(entry)
            else:
                if self.children[2]:
                    if entry <= self.children[2].entry:
                        self.children[2].removeEntry(entry)
                    else:
                        if self.children[3]:
                            self.children[3].removeEntry(entry)
                        else:
                            raise TreeValueDoesNotExist(entry)
                else:
                    raise TreeValueDoesNotExist(entry)


tree = None
option = '0'
while option != '5':
    option = input("1. Create tree\n2. Add value to tree\n3. Remove value from tree\n4. Print tree\n5. Exit\n")
    entry = None
    try:
        if option == '1':
            entry = int(input("please insert entry\n"))
            tree = NaryTree(entry)
        elif option == '2':
            if tree:
                entry = int(input("please insert entry\n"))
                tree.addEntry(entry)
            else:
                raise UnboundLocalError
        elif option == '3':
            if tree:
                entry = int(input("please insert entry\n"))
                tree.removeEntry(entry)
            else:
                raise UnboundLocalError
        elif option == '4':
            print(str(tree))
        elif option != '5':
            print("invalid option, please select a number from 1 to 5")
    except UnboundLocalError:
        print("error. please create the tree first (option 1)")
    except TreeIllegalValue:
        print(f"error. the requested value {entry} is not a leaf in the tree.\n {str(tree)}")
    except TreeValueDoesNotExist:
        print(f"error. the requested value {entry} does not exist in the tree.\n {str(tree)}")
    except:
        print("error")
        option = '5'