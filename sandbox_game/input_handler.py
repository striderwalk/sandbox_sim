import sys

import pygame

from sandbox.objects.fountain import Fountain

result_map = {
    pygame.K_LSHIFT: {"handler": "settings", "type": "toggle_play"},
    pygame.K_ESCAPE: {"handler": "main", "type": "menu"},
    pygame.K_RETURN: {"handler": "main", "type": "update"},
    pygame.K_TAB: {"handler": "selection", "type": "right"},
    pygame.K_LEFT: {"handler": "selection", "type": "left"},
    pygame.K_RIGHT: {"handler": "selection", "type": "right"},
    pygame.K_LCTRL: {"handler": "selection", "type": "left"},
    pygame.K_t: {"handler": "settings", "type": "temp"},
    pygame.K_r: {"handler": "main", "type": "reset"},
    pygame.K_q: {"handler": "sim", "type": "fix"},
}


def process_event(event, mouse, selected):
    result = []
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_SPACE:
            result.append({"handler": "sim", "type": "rain", "value": selected})

        elif event.key in result_map:
            # get rid of endless elif
            result.append(result_map[event.key])

    # change press size
    if event.type == pygame.MOUSEBUTTONDOWN:
        # up
        if event.button == 4:
            mouse.scale(1)
        if event.button == 5:
            mouse.scale(-1)

    return result


def process_events(events, mouse, selected):
    result = []

    _process_event = lambda event: process_event(event, mouse, selected)
    for i in list(map(_process_event, events)):
        result.extend(i)

    return result


def input_handle(mouse, board, selected):
    mouse_val = mouse.get_pos()
    keys = pygame.key.get_pressed()
    clicks = []

    if keys[pygame.K_k]:
        clicks.append({"handler": "sim", "type": "heat", "value": [50, mouse.size]})

    if keys[pygame.K_j]:
        clicks.append({"handler": "sim", "type": "heat", "value": [-50, mouse.size]})

    if keys[pygame.K_e]:  # place fountain
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            clicks.append(
                {
                    "handler": "sim",
                    "type": "press",
                    "value": (mouse.size, x, y, Fountain, False, selected),
                }
            )
    events = list(pygame.event.get())
    result = process_events(events, mouse, selected)
    return clicks, result
