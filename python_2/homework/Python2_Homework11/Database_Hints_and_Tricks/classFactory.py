'''
classFactory: function to return tailored classes
'''

def build_row(table, *cols, curs, condition):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data)==len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))

        def retrieve(self, curs, condition=None):
            """ 
            retrieve a single record or multiple records
            based on the condition given
            """
            if condition:
                sql = "select * from animal where " + condition
            else:
                sql = "select * from animal"
            curs.execute(sql)

            for data in curs.fetchall():
                yield DataRow(data)

    DataRow.table = table
    DataRow.cols = cols
    return DataRow