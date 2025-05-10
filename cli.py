import cmd
from controller import Controller
from visualizer import draw_graph

controller = Controller()

class ControllerCLI(cmd.Cmd):
    intro = "SDN controller CLI\n"
    prompt = 'SDN: '

    def do_add_node(self, arg):
        controller.topology.add_node(arg)
        print(f"Node {arg} added.")

    def do_add_link(self, arg):
        n1, n2 = arg.split()
        controller.topology.add_link(n1, n2)
        print(f"Link {n1} to {n2} added.")

    def do_inject_traffic(self, arg):
        src, dst = arg.split()
        controller.inject_traffic(src, dst)

    def do_fail_link(self, arg):
        n1, n2 = arg.split()
        controller.simulate_link_failure((n1, n2))

    def do_show_flows(self, arg):
        draw_graph(controller.topology.graph, controller.active_flows)

    def do_exit(self, arg):
        print("Exiting SDN CLI.")
        return True

if __name__ == '__main__':
    ControllerCLI().cmdloop()
