CREATE TABLE IF NOT EXISTS movie (
  id         INT           NOT NULL PRIMARY KEY AUTO_INCREMENT
  COMMENT 'id 自增',
  name       VARCHAR(512)  NOT NULL
  COMMENT '名称',
  movieInfo  VARCHAR(1024) NOT NULL
  COMMENT '详情',
  star       VARCHAR(512)                       DEFAULT NULL
  COMMENT '评分',
  quote      VARCHAR(1024)                      DEFAULT NULL
  COMMENT '经典台词',
  created_at TIMESTAMP                          DEFAULT current_timestamp
  COMMENT '添加时间'
)
  ENGINE = InnoDB
  DEFAULT CHARSET = UTF8;