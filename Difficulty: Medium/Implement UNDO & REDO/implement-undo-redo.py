class Solution:
    def __init__(self):
        self.doc = []
        self.redo_stack = []
    def append(self, x):
        # append x into document
        self.doc.append(x)
        self.redo_stack.clear()

    def undo(self):
        # undo last change
        if self.doc:
            self.redo_stack.append(self.doc.pop())

    def redo(self):
        # redo changes
        if self.redo_stack:
            self.doc.append(self.redo_stack.pop())

    def read(self):
        # read the document
        return "".join(self.doc)