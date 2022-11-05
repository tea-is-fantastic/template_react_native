from post import post
from pre import pre
from run import run
from actions.action_templates import template_exit, template_init

if __name__ == '__main__':
    template_init()
    pre()
    run()
    post()
    template_exit()
