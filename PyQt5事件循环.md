#  Qt事件循环

在事件循环中，不停地去获取下一个事件，然后做出处理。

事件存储的地方，操作系统存储，软件存储

事件队列 Event Queue

处理事件 也叫事件分发 Event Dispatch

Linux X11窗口系统，事件循环

```c
Atom wmDeleteMessage = XInternAtom(mDisplay, "WM_DELETE_WINDOW", False);
XSetWMProtocols(display, window, &wmDeleteMessage, 1);

XEvent event;
bool running = true;

while (running)
{
    XNextEvent(display, &event);

    switch (event.type)
    {
        case Expose:
            printf("Expose\n");
            break;

        case ClientMessage:
            if (event.xclient.data.l[0] == wmDeleteMessage)
                running = false;
            break;

        default:
            break;
    }
}
```



`QEventLoop`

```c
int exec(QEventLoop::ProcessEventsFlags flags = AllEvents)
void exit(int returnCode = 0)
bool isRunning() const
bool processEvents(QEventLoop::ProcessEventsFlags flags = AllEvents)
void processEvents(QEventLoop::ProcessEventsFlags flags, int maxTime)
void wakeUp()
```

`exec`是启动事件循环，调用exec后，调用exec的函数会被阻塞，直到`EventLoop`里的while循环结束







![preview](https://pic1.zhimg.com/v2-00ab750f452a75b744c7224f6552cae4_r.jpg)





`exit`是退出事件循环

`Application`类关键是维护了一个`QEventLoop`

主事件循环

`Application`提供两个函数`sendEvent`,`poseEvent`,前者是立即处理事件，后者则将事件加入事件队列，下一轮事件循环才处理







