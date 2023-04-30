import tkinter as tk
from tkinter.font import Font


class DblUnderlineLabel(tk.Canvas):
    def __init__(self, master, **kw):
        # collect text's properties
        font = Font(master, kw.pop('font', ''))
        text = kw.pop('text', '')
        if 'fg' in kw:
            fg = kw.pop('fg')
        else:
            fg = kw.pop('foreground', 'black')
        # initialize the canvas
        tk.Canvas.__init__(self, master, **kw)
        # display the text
        self.create_text(2, 2, anchor='nw', font=font, text=text, fill=fg, tags='text')
        h = font.metrics('linespace')  # font property needed to position correctly the underlining
        bbox = self.bbox('text')  # get text bounding box in the canvas
        w = font.actual('size')//8  # scale thickness of the underling with font size
        # create the double underlining
        self.create_line(bbox[0], h - 1, bbox[2], h - 1, fill=fg, width=w, tags='line')
        self.create_line(bbox[0], h + int(1.1*w), bbox[2], h + int(1.1*w), fill=fg, width=w,
                         tags='line')
        # resize the canvas to fit the text
        bbox = self.bbox('all')
        self.configure(width=bbox[2], height=bbox[3])


root = tk.Tk()
for size in [12, 18, 32, 64]:
    DblUnderlineLabel(root, text="Arial %i bold" % size, font="Arial %i bold" % size).pack()
root.mainloop()
