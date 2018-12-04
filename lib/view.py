import pygame
import time
from cell_field  import Cell_Field
from region  import Region
from point  import Point

class View:
    
    def __init__(self):
#init cell field
        self.c = Cell_Field(500, 500)

#init pygame rendering
        self.screen = pygame.display.set_mode((500, 500))

        pygame.font.init()
        self.game_font = pygame.font.SysFont('Terminus', 30)
        self.prompt_text = "Click to place obstacles"
        self.message_surface = self.game_font.render(self.prompt_text, False, (0, 0, 0))

#init world tracking/logic
        self.point_index = 0
        self.placement_counter = 0
        self.draw_path = False
        self.obstacle_sizes = [(200, 200), (150,150), (100, 100)]
        self.start_point = Point(0,0)
        self.end_point = Point(0,0)
    
        self.update_window()

    def set_prompt_text(self, prompt_string):
        self.message_surface = game_font.render(prompt_string, False, (0, 0, 0))
        
    def update_window(self):
        
#draw the background 
        self.screen.fill((255, 255, 255))

#draw text prompts 
        self.message_surface = self.game_font.render(self.prompt_text, False, (0, 0, 0))
        self.screen.blit(self.message_surface, (0, 0))
#draw the obstacles
        for obstacle in self.c.obstacles:
            pygame.draw.rect(self.screen, (255, 0, 0), (obstacle.x, obstacle.y, obstacle.w, obstacle.h))

#draw the navigation points
        if self.draw_path:
            pygame.draw.circle(self.screen, (255, 0, 0), (self.start_point.x, self.start_point.y), 5)
            pygame.draw.circle(self.screen, (0, 0, 255), (self.end_point.x, self.end_point.y), 5)

            for i in range (0, self.point_index):
                pygame.draw.circle(self.screen, (0, 255, 0), (self.point_list[i].x, self.point_list[i].y), 5)
            
            for i in range (1, self.point_index):
                pygame.draw.line(self.screen, (0, 0, 255), (self.point_list[i].x, self.point_list[i].y),
                                 (self.point_list[i-1].x, self.point_list[i-1].y))
            self.point_index += 1
            if self.point_index > len(self.point_list):
                self.point_index = len(self.point_list)

#update the screen
        pygame.display.flip()
        time.sleep(0.25)


    def set_start_point(self):
        mouse_pos = pygame.mouse.get_pos()
        print("set start point to", mouse_pos)
        self.start_point = Point(mouse_pos[0], mouse_pos[1])


    def set_end_point(self):
        mouse_pos = pygame.mouse.get_pos()
        print("set end point to", mouse_pos)
        self.end_point = Point(mouse_pos[0], mouse_pos[1])


    def create_obstacle(self, width, height):
        mouse_pos = pygame.mouse.get_pos()
        new_obstacle = Region(mouse_pos[0], mouse_pos[1], width, height) 
        self.c.obstacles.append(new_obstacle)
        if self.placement_counter == 2:
            self.prompt_text = "Click to set start point"

        
    def handle_user_mouse(self):
        if self.placement_counter <= 2:
            curr_size = self.obstacle_sizes[self.placement_counter]
            self.create_obstacle(curr_size[0], curr_size[1])
            self.placement_counter += 1

        elif self.placement_counter == 3:
            self.set_start_point()
            self.placement_counter += 1
            self.prompt_text = "Click to set goal point"

        else:
            self.point_index = 0
            self.placement_counter = 3

            self.prompt_text = "Click to set start point"
            self.set_end_point()

            self.c.determine_regions()
            self.c.construct_graph()

            self.draw_path = True
            self.point_list = self.c.navigate(self.start_point, self.end_point)

        self.update_window()


def main():
    view = View()
    
    running = True
    while running:
        view.update_window()

#handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                view.handle_user_mouse()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    view = View()
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
