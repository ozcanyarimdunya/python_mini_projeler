import uuid


class Todo:
    def __init__(self, name, done=False):
        """
        Initialize a new uuid.

        Args:
            self: (todo): write your description
            name: (str): write your description
            done: (int): write your description
        """
        self.id = str(uuid.uuid4()).split('-')[0]
        self.name = name
        self.done = done

    def __repr__(self):
        """
        Return a repr representation of a repr__.

        Args:
            self: (todo): write your description
        """
        return f"{self.id} {self.name}({'✔️' if self.done else '❌'})"


class Repository(list):

    def append(self, todo: Todo):
        """
        Add a todoist to the list.

        Args:
            self: (todo): write your description
            todo: (str): write your description
        """
        for _todo in self:
            if _todo.id == todo.id:
                return

        super(Repository, self).append(todo)

    def update(self, todo: Todo):
        """
        Updates the list of a todoist.

        Args:
            self: (todo): write your description
            todo: (todo): write your description
        """
        for _todo in self:
            if _todo.id == todo.id:
                _todo.name = todo.name
                _todo.done = todo.done
                return
        else:
            raise Exception("No such todo!")

    def delete(self, todo: Todo):
        """
        Delete a todo item.

        Args:
            self: (todo): write your description
            todo: (str): write your description
        """
        for _todo in self:
            if _todo.id == todo.id:
                self.remove(_todo)
                return
        else:
            raise Exception("No such todo!")


repo = Repository()


def add(*todos):
    """
    Add a list of todos

    Args:
        todos: (int): write your description
    """
    if len(todos) == 1:
        repo.append(*todos)
    else:
        for todo in todos:
            repo.append(todo)


def update(*todos):
    """
    Updates the list of lists todo

    Args:
        todos: (todo): write your description
    """
    if len(todos) == 1:
        repo.update(*todos)
    else:
        for todo in todos:
            repo.update(todo)


def delete(*todos):
    """
    Deletes the given tables.

    Args:
        todos: (str): write your description
    """
    if len(todos) == 1:
        repo.delete(*todos)
    else:
        for todo in todos:
            repo.delete(todo)


if __name__ == '__main__':
    t = Todo("Go home")
    t2 = Todo("Go shopping")
    t3 = Todo("Go school")

    add(t, t2, t3)
    print(repo)
    # [0d5b07a4 Go home(❌), 676ef76e Go shopping(❌), 7f46f32d Go school(❌)]

    t.done = True
    t2.done = True
    update(t, t2)
    print(repo)
    # [0d5b07a4 Go home(✔️), 676ef76e Go shopping(✔️), 7f46f32d Go school(❌)]

    delete(t2, t3)
    print(repo)
    # [0d5b07a4 Go home(✔️)]
