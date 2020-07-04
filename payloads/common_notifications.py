import libslobs.payloads.common_payloads as common_payloads

class SLOBSNotificationsService(common_payloads.SLOBSPayloads):
    def __init__(self):
        common_payloads.SLOBSPayloads.__init__(self)
        self.resource = "NotificationsService"

    def applyAction(self, notificationId):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "applyAction",
            "params": {
                "resource": self.resource,
                "args": [notificationId]
            }
        }

    def getAll(self, notificationType):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getAll",
            "params": {
                "resource": self.resource,
                "args": [notificationType]
            }
        }

    def getNotification(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getNotification",
            "params": {
                "resource": self.resource,
                "args": [id]
            }
        }

    def getRead(self, notificationType):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getRead",
            "params": {
                "resource": self.resource,
                "args": [notificationType]
            }
        }

    def getSettings(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getSettings",
            "params": {
                "resource": self.resource,
            }
        }

    def getUnread(self, notificationType):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "getUnread",
            "params": {
                "resource": self.resource,
                "args": [notificationType]
            }
        }

    def markAllAsRead(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "markAllAsRead",
            "params": {
                "resource": self.resource
            }
        }

    def markAsRead(self, id):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "markAsRead",
            "params": {
                "resource": self.resource,
                "args": [id]
            }
        }

    def push(self, notifyInfo):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "push",
            "params": {
                "resource": self.resource,
                "args": [notifyInfo]
            }
        }

    def restoreDefaultSettings(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "restoreDefaultSettings",
            "params": {
                "resource": self.resource
            }
        }

    def setSettings(self, patch):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "setSettings",
            "params": {
                "resource": self.resource,
                "args": [patch]
            }
        }

    def showNotifications(self):
        return {
            "jsonrpc": "2.0",
            "id": self.token,
            "method": "showNotifications",
            "params": {
                "resource": self.resource
            }
        }