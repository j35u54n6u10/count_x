import flet as ft


def main(page: ft.Page):

    def x_count(e):
        while input_sn.value < input_en.value:
            sn = int(input_sn.value)
            sn += 1
            print(f"X{sn}")
            #input_sn.value = int(input_sn.value) + 1
            #show_count.value = "X" + str(input_sn.value)

    def x_count_test (e):
        while input_sn.value < input_en.value:
            input_sn.value = input_sn.value + 1
            print(f"X{input_sn.value}")
           

    title_x = ft.Text("X Counter", size=25)
    # Start number
    #text_sn = ft.Text("Enter start number:", size=12, weight=ft.FontWieght.W_100)
    input_sn = ft.TextField(label="Start number")
    # End number
    #text_en = ft.Text ("Enter end number:", size=12, weight=ft.FontWieght.W_100)
    input_en = ft.TextField(label="End number")

    # Generate botton
    gene_botton = ft.CupertinoFilledButton(content=ft.Text("Generate"), 
                                           opacity_on_click=0.5,
                                           on_click= x_count_test)
    # Show count
    show_count = ft.TextField(label="Count", read_only=True)

    #copy botton
    copy_botton = ft.CupertinoFilledButton(content=ft.Text("Copy"),
                                           opacity_on_click=0.5,
                                           on_click= print("Copy"))


    page.add(title_x, input_sn, input_en, gene_botton, show_count, copy_botton)

ft.app(main)
