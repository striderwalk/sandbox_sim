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
}


def process_event(event, game) -> list:
    result = []
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_SPACE:
            result.append(
                {"handler": "sim", "type": "rain", "value": game.selection.selected}
            )

        elif event.key in result_map:
            # get rid of endless elif
            result.append(result_map[event.key])

    # change press size
    if event.type == pygame.MOUSEBUTTONDOWN:
        # up
        if event.button == 4:
            game.mouse.scale(1)
        if event.button == 5:
            game.mouse.scale(-1)

    return result


def process_events(events, game):
    result = []

    _process_event = lambda event: process_event(event, game)
    for i in list(map(_process_event, events)):
        result.extend(i)

    return result


def input_handle(game):
    mouse_val = game.mouse.get_pos()
    keys = pygame.key.get_pressed()
    events = []

    if keys[pygame.K_k]:
        events.append(
            {"handler": "sim", "type": "heat", "value": [50, game.mouse.size]}
        )

    if keys[pygame.K_j]:
        events.append(
            {"handler": "sim", "type": "heat", "value": [-50, game.mouse.size]}
        )

    if keys[pygame.K_e]:  # place fountain
        if mouse_val[0] == "BOX":
            x, y = mouse_val[1:]
            events.append(
                {
                    "handler": "sim",
                    "type": "press",
                    "value": (
                        game.mouse.size,
                        x,
                        y,
                        Fountain,
                        False,
                        game.selection.selected,
                    ),
                }
            )
    if keys[pygame.K_q]:
        events.append({"handler": "sim", "type": "fix"})

    pygame_events = list(pygame.event.get())

    events = process_events(pygame_events, game)

    return events
