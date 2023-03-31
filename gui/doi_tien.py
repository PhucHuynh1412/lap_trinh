import PySimpleGUI as sg

sg.theme('LightBlue2')  # Chọn theme cho giao diện

layout = [[sg.Text('Amount:'), sg.InputText(key='amount')],
          [sg.Text('From currency:'), sg.Combo(['USD', 'EUR', 'GBP', 'JPY'], key='from_currency')],
          [sg.Text('To currency:'), sg.Combo(['USD', 'EUR', 'GBP', 'JPY'], key='to_currency')],
          [sg.Button('Exchange'), sg.Button('Reset')]]

window = sg.Window('Exchange Form', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Exchange':
        amount = values['amount']
        from_currency = values['from_currency']
        to_currency = values['to_currency']
        # Thực hiện việc đổi tiền tại đây
        sg.popup(f"{amount} {from_currency} = {result} {to_currency}")
    if event == 'Reset':
        window.find_element('amount').Update('')
        window.find_element('from_currency').Update('USD')
        window.find_element('to_currency').Update('USD')

window.close()

