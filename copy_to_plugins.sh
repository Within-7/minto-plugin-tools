#!/bin/bash

# 定义目标目录
TARGET_DIR=".minto/plugins"

# 创建目标目录（如果不存在）
mkdir -p "$TARGET_DIR"

# 获取当前脚本所在目录
CURRENT_DIR="$(pwd)"

# 遍历当前目录下的所有子目录
for dir in */; do
    # 移除末尾的斜杠
    dir_name="${dir%/}"
    
    # 跳过隐藏目录和脚本自身
    if [[ "$dir_name" == .* ]] || [[ "$dir_name" == *.sh ]]; then
        continue
    fi
    
    # 跳过目标目录本身
    if [[ "$dir_name" == ".minto" ]]; then
        continue
    fi
    
    # 检查是否是目录
    if [ -d "$dir_name" ]; then
        echo "正在拷贝: $dir_name -> $TARGET_DIR/"
        cp -r "$dir_name" "$TARGET_DIR/"
    fi
done

echo "拷贝完成！"
