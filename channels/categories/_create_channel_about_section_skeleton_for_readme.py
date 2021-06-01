from selenium import webdriver

def main(url):
    driver = webdriver.Firefox()
    with driver:
        driver.get(f'{url}/about')
        extract_text(driver)
        input('Hit enter to close the window after you pull out any additional information you want from the page...\n')


def extract_text(driver):
    channel_name           = driver.find_element_by_id('text-container').text
    formatted_channel_name = channel_name.replace(' ', '').replace('/', '-')
    description = driver.find_element_by_id('description').text
    biography   = driver.find_element_by_id('bio-container').text
    details     = driver.find_element_by_id('details-container').text
    links       = driver.find_element_by_id('links-container').text
    open_expandable_section_tag   = f'<details>\n<summary><strong>{channel_name}'
    finish_expandable_section_tag =  '</strong></summary>\n'
    with open(f'{formatted_channel_name}.md', mode='w', newline=None, encoding='utf-8') as file:
        file.write(f'## {channel_name}\n')
        file.write(f'{open_expandable_section_tag}: About Page{finish_expandable_section_tag}\n')
        file.write(f'{open_expandable_section_tag} Description{finish_expandable_section_tag}{description}\n</details>\n\n')
        file.write(f'{open_expandable_section_tag} Biography{finish_expandable_section_tag}{biography}\n</details>\n\n')
        file.write(f'{open_expandable_section_tag} Details{finish_expandable_section_tag}{details}\n</details>\n\n')
        file.write(f'{open_expandable_section_tag} Links{finish_expandable_section_tag}{links}\n</details>\n\n')
        file.write('</details>')


if __name__ == '__main__':
    url = input('ENTER THE URL TO THE YOUTUBE CHANNEL YOU WANT TO CREATE THE ABOUT SECTION FOR BELOW.\nAcceptable formats\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw/\n\nNOT acceptable formats:\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw/videos\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw/playlists\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw/community\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw/chanels\n  https://www.youtube.com/channel/UCpjlh0e319ksmoOD7bQFSiw/about\n\n')
    main(url)
