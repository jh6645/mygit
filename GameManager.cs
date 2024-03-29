﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Snake_Game
{
    public class GameManager
    {
        private Map _map;
        private Snake _snake;
        private Food _food;

        private int _mapSize = 25;
        private int _sumTick = 0;

        private const int WAIT_TICK = 1000 / 10;
        private const int MOVE_TICK = 1000;

        public void StartGame()
        {
            _map = new Map();
            _snake = new Snake();
            _food = new Food();
            
            _map.Initialize(_mapSize);
            _snake.Initialize(10, 12);
            _food.CreateFood(5, 5);

            Console.CursorVisible = false;
            int lastTick = 0;
            while (true)
            {
                #region 프레임 관리
                // 만약에 경과한 시간이 1/30초보다 작다면
                int currentTick = System.Environment.TickCount;
                if (currentTick - lastTick < WAIT_TICK)
                    continue;

                int deltaTick = currentTick - lastTick;
                lastTick = currentTick;
                #endregion


                Console.SetCursorPosition(0, 0);

                if (IsGameOver())
                {
                    Console.Clear();
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("\n\n\nGame Over");
                    break;
                }

                ConsoleKeyPressCheck();

                SnakeEatFoodCheck();


                _sumTick += deltaTick;
                if (_sumTick >= MOVE_TICK)
                {
                    _snake.MoveSnake();
                    _map.Render(_snake.Positions, _food.Position);
                }
            }
        }

        private void SnakeEatFoodCheck()
        {
            if (_snake.Positions[0].Y == _food.Position.Y && _snake.Positions[0].X == _food.Position.X)
            {
                _snake.EatFood(_food.Position);
                _food.RespawnFood();
            }
        }

        private void ConsoleKeyPressCheck()
        {
            if (Console.KeyAvailable)
            {
                ConsoleKeyInfo consoleKey = Console.ReadKey();

                switch (consoleKey.Key)
                {
                    case ConsoleKey.LeftArrow:
                        _snake.SwitchDirection(Snake.Dir.Left);
                        break;
                    case ConsoleKey.RightArrow:
                        _snake.SwitchDirection(Snake.Dir.Right);
                        break;
                    case ConsoleKey.UpArrow:
                        _snake.SwitchDirection(Snake.Dir.Up);
                        break;
                    case ConsoleKey.DownArrow:
                        _snake.SwitchDirection(Snake.Dir.Down);
                        break;
                    case ConsoleKey.Q:
                        return;
                }
            }
        }

        private bool IsGameOver()
        {
            int headPosY = _snake.Positions[0].Y;
            int headPosX = _snake.Positions[0].X;

            if (headPosY <= -1 || headPosY >= _map.Size || headPosX <= -1 || headPosX >= _map.Size)
                return true;

            for (int i = 1; i < _snake.Positions.Count; i++)
            {
                if (headPosY == _snake.Positions[i].Y && headPosX ==  _snake.Positions[i].X)
                    return true;
            }

            return false;
        }
    }
}