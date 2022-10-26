    save = load_save()
    control_handler = Controls_Handler(save)
    actions = {"Left": False, "Right": False, "Up": False, "Down": False, "Start": False, "Action1": False}
    running = True
    while running:
    ################################# CHECK PLAYER INPUT #################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = True
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = True
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = True
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = True
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = True
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = True

            if event.type == pygame.KEYUP:
                if event.key == control_handler.controls['Left']:
                    actions['Left'] = False
                if event.key == control_handler.controls['Right']:
                    actions['Right'] = False
                if event.key == control_handler.controls['Up']:
                    actions['Up'] = False
                if event.key == control_handler.controls['Down']:
                    actions['Down'] = False
                if event.key == control_handler.controls['Start']:
                    actions['Start'] = False
                if event.key == control_handler.controls['Action1']:
                    actions['Action1'] = False

        ################################# UPDATE THE GAME #################################
        control_handler.update(actions)
        ################################# RENDER WINDOW AND DISPLAY #################################
        canvas.fill(("white"))
        control_handler.render(canvas)
        screen.blit(pygame.transform.scale(canvas, (1280,720) ), (0,0))
        pygame.display.update()
        reset_keys(actions)