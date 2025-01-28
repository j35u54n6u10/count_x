import flet as ft


def main(page: ft.Page):

    def x_count(e):
        sequence = ""
        for i in range (int(input_sn.value, int(input_en.value) + 1)):
            sequence += f"X{str(int(input_sn.value))} \n"
            text_count.value = sequence
            page.update()

        # while int(input_sn.value) < int(input_en.value):
        #
        #     input_sn.value = int(input_sn.value) + 1
        #     # show_count.value = "X" + str(int(input_sn.value)) + "\n"
        #     text_count.value = f"X{str(int(input_sn.value))}\n"
        #
        #     text_count.update()
        #
        

    title_x = ft.Text("X Counter", size=25)
    # Start number
    #text_sn = ft.Text("Enter start number:", size=12, weight=ft.FontWieght.W_100)
    input_sn = ft.TextField(label="Start number")
    # End number
    #text_en = ft.Text ("Enter end number:", size=12, weight=ft.FontWieght.W_100)
    input_en = ft.TextField(label="End number")
    text_count = ft.TextField(value="", text_size=15, multiline=True, read_only=True) 
    # Generate botton
    gene_botton = ft.CupertinoFilledButton(content=ft.Text("Generate"), 
                                           opacity_on_click=0.5,
                                           on_click= x_count)
    # Show count
    show_count = ft.TextField(label="Count", read_only=True)

    #copy botton
    copy_botton = ft.CupertinoFilledButton(content=ft.Text("Copy"),
                                           opacity_on_click=0.5,
                                           on_click= lambda e: page.set_clipboard(text_count.value))


    page.add(title_x, input_sn, input_en, gene_botton, text_count, copy_botton)

ft.app(main)
