//
//  AppDelegate.m
//  iOS_Confusion
//
//  Created by fuyongYU on 2018/6/21.
//  Copyright © 2018年 夜猫子. All rights reserved.
//

#import "AppDelegate.h"

//需要声明此方法
extern void impl_ref_to_all_class();

@interface AppDelegate ()

@end

@implementation AppDelegate


- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    
    //系统启动的地方进行调用，不调用是没发打包进iPA包里面的
    try {
        // 如果不使用研发提供的混淆代码工具，请注释调这行代码
        impl_ref_to_all_class();
    } catch (NSException *e) {
        NSLog(@"exception...");
    }
    
    /**
     如果是直接导出的母工程可以使用以下代码，我这里就没有导母工程，代码如下
     try {
     impl_ref_to_all_class();
     } catch (NSException *e) {
     NSLog(@"exception");
     }
     */
    
    
    
    return YES;
}


- (void)applicationWillResignActive:(UIApplication *)application {
    // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
    // Use this method to pause ongoing tasks, disable timers, and invalidate graphics rendering callbacks. Games should use this method to pause the game.
}


- (void)applicationDidEnterBackground:(UIApplication *)application {
    // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
    // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
}


- (void)applicationWillEnterForeground:(UIApplication *)application {
    // Called as part of the transition from the background to the active state; here you can undo many of the changes made on entering the background.
}


- (void)applicationDidBecomeActive:(UIApplication *)application {
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
}


- (void)applicationWillTerminate:(UIApplication *)application {
    // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
}


@end
