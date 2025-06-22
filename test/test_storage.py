from src.utils.logger import Logger
from src.utils.storage import Storage

logger = Logger(__name__)


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
    "article": """CREATE TABLE IF  NOT  EXISTS `article` (
                    `article_id` INT NOT NULL AUTO_INCREMENT COMMENT '文章ID（主键）',
                    `subset_id` INT NOT NULL COMMENT '文章分类（外键关联 subset 表）',
                    `user_id` INT NOT NULL COMMENT '作者用户ID（外键关联 user 表）',
                    `title` VARCHAR(255) NOT NULL COMMENT '文章名称',
                    `content` TEXT NOT NULL COMMENT '文章内容',
                    `img_src` VARCHAR(500) DEFAULT '' COMMENT '封面图片地址（默认为空）',
                    `state` BOOLEAN NOT NULL DEFAULT FALSE COMMENT '文章状态：FALSE-未发布，TRUE-已发布',
                    `create_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
                    `read_count` INT NOT NULL DEFAULT 0 COMMENT '阅读次数（默认0）',
                    
                    PRIMARY KEY (`article_id`),
                    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`) ON DELETE CASCADE,
                    FOREIGN KEY (`subset_id`) REFERENCES `subset`(`subset_id`) ON DELETE RESTRICT
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章信息表'""",
}


class TestStorage:

    def test_storage(self):
        sql: str = "SELECT * FROM `user`;"
        with Storage() as storage:
            results = storage.query_all(sql)
            assert len(results) > 0

    def test_init_mysql(self):
        def create_table(sql: str):
            with Storage() as storage:
                storage.save(sql)

        create_table(tables["user"])
        create_table(tables["subset"])
        create_table(tables["article"])
        logger.debug("创建数据表SQL语句运行成功")
