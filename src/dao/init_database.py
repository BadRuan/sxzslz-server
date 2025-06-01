from src.utils.storage import Storage


tables = {
    "user": """CREATE TABLE IF NOT EXISTS `user` (
                    `user_id` INT NOT NULL AUTO_INCREMENT COMMENT '用户ID（主键）',
                    `user_name` VARCHAR(50) NOT NULL COMMENT '用户名（唯一）',
                    `nick_name` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '昵称（默认为空）',
                    `password` VARCHAR(255) NOT NULL COMMENT '加密后的密码',
                    `avatar_src` VARCHAR(500) NOT NULL DEFAULT '' COMMENT '头像地址（默认为空）',
                    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
                    
                    PRIMARY KEY (`user_id`),
                    UNIQUE KEY  (`user_name`) 
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表'""",
    "subset": """CREATE TABLE IF NOT EXISTS `subset` (
                    `subset_id` INT NOT NULL AUTO_INCREMENT COMMENT '分类ID（主键）',
                    `subset_name` VARCHAR(50) NOT NULL COMMENT '分类名称（唯一）',
                    `subset_type` INT NOT NULL DEFAULT '1' COMMENT '所属类型（默认为空）',
                    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
                    
                    PRIMARY KEY (`subset_id`),
                    UNIQUE KEY  (`subset_name`) 
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='分类信息表' """,
}


def init_database():
    def create_table(sql: str):
        with Storage() as storage:
            storage.save(sql)

    create_table(tables["user"])
    create_table(tables["subset"])
