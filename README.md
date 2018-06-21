 # iOS最新混淆代码

> 需要在AppDelegate.mm（Unity转换过来的母工程是UnityAppController.mm）中使用

>此Demo使用的是直接创建的项目，并非是Unity转换过来的母工程

>此处以AppDelegate.mm介绍，在UnityAppController.mm同理，具体可以看Demo

```
需要声明垃圾代码
//需要声明此方法
extern void impl_ref_to_all_class();

以下在以下方法里面进行实现声明的方法即可
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    //系统启动的地方进行调用，不调用是没发打包进iPA包里面的
    try {
    // 如果不使用研发提供的混淆代码工具，请注释调这行代码
        impl_ref_to_all_class();
    } catch (NSException *e) {
        NSLog(@"exception...");
    }

    /**
    如果是直接导出的母工程可以使用以下代码，我这里就没有导母工程，代码如下,以下是在UnityAppController.mm可如下使用：
    try {
        impl_ref_to_all_class();
    } catch (NSException *e) {
        NSLog(@"exception");
    }
    */



    return YES;
}


```

>使用提供的Python文件（RandomCodeTools.py）就可以使用文件夹是recode的垃圾代码，直接拖          入工程即可，建议生成垃圾代码控制在50-100个类左右，过多还是容易被苹果4.3。
>如下截图介绍
![image](https://github.com/zhongaiyemaozi/iOS-confusion/blob/master/WechatIMG229.jpeg)

 ## 反馈与建议
- 邮箱：<873456034@qq.com>

---------
感谢阅读这份帮助文档。若帮助到了你请点击右上角star。


