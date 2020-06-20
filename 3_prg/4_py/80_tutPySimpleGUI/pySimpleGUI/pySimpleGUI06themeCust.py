import PySimpleGUI as sg
# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#709053',
                                        'TEXT': '#fff4c9',
                                        'INPUT': '#c7e78b',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#709053'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
# Switch to use your newly created theme
sg.change_look_and_feel('MyNewTheme')
# Call a popup to show what the theme looks like
sg.popup_get_text('This how the MyNewTheme custom theme looks')
