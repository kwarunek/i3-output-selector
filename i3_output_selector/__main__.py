#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import partial
import i3

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class OutputSelector(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Select output")
        self.parent.call('wm', 'attributes', '.', '-type', 'dialog')
        self.parent.bind('<Escape>', self.close)
        self.pack(fill=tk.BOTH, expand=0)

        outputs = i3.get_outputs()
        ws_output = self.get_current_workspace_output()

        for idx, output in enumerate(outputs):
            cmd = partial(self.move_to, output['name'])
            tk.Button(
                self.parent, text='%s (Alt + %s)' % (output['name'], idx),
                state=(tk.NORMAL if output['active'] else tk.DISABLED),
                relief=(tk.SUNKEN if ws_output == output['name'] else tk.RAISED),
                command=cmd
            ).pack(fill=tk.X)
            self.parent.bind('<Alt-KeyPress-%s>' % idx, cmd)

        tk.Button(
            self.parent, text='Quit (Esc)', command=self.parent.destroy
        ).pack(fill=tk.X, side=tk.BOTTOM)

    def move_to(self, output, event=None):
        i3.command('move', 'workspace to output %s' % output)
        self.parent.destroy()

    def get_current_workspace_output(self):
        workspaces = i3.get_workspaces()
        current_workspace = list(filter(lambda s: s['focused'] is True, workspaces))[0]
        return current_workspace['output']

    def close(self, *args, **kwargs):
        self.parent.destroy()


def main():
    root = tk.Tk()
    OutputSelector(root)
    root.mainloop()


if __name__ == '__main__':
    main()
