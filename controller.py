import logger
import model
import view

def run():
    while True:
        mode = view.work_mode()
        if mode == '1':
            contact = view.info_people()
            logger.add_new(contact)
        elif mode == '2':
            contact = view.info_for_search()
            base = logger.get_base()
            result = model.search_contact(base, contact)
            view.search_result(result)
            
            
            