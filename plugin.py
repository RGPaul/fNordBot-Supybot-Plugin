###
# Copyright (c) 2010, Ralph-Gordon Paul
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import supybot.ircdb as ircdb


class fNord(callbacks.Plugin):
    """This plugin provides a few functions used for the channel #fnordeingang."""
    def __init__(self, irc):
        self.__parent = super(fNord, self)
        self.__parent.__init__(irc)
        self.homepage_url = 'http://www.fnordeingang.de'
        self.greetings_enable = False

    # homepage command returns homepage
    # Todo: set homepage command
    def homepage(self, irc, msg, args):
        """takes no arguments

        Returns the homepage for this channel.
        """
        irc.reply(self.homepage_url)
    homepage = wrap(homepage)

    # actions if someone joins the channel
    # at the moment it greets the joined user
    def doJoin(self, irc, msg):
        if self.greetings_enable and irc.nick != msg.nick: # don't greet hisself
            # msg.args[0] contains Channel Name
            irc.queueMsg(ircmsgs.privmsg(msg.args[0], 'Moin %s' % msg.nick))
        irc.noReply()

    def greetings(self, irc, msg, args, mod):
        """[<enable|disable>]

        Enables or disables Greetings. By default it returns it's state.
        Greetings are disabled by default.
        """

        if mod == "enable":
            self.greetings_enable = True
            irc.reply('Greetings enabled')
        elif mod == "disable":
            self.greetings_enable = False
            irc.reply('Greetings disabled')
        else:
            if self.greetings_enable:
                irc.reply('Greetings are enabled')
            else:
                irc.reply('Greetings are disabled')
    greetings = wrap(greetings, [optional('anything'), 'admin'])

    def test(self, irc, msg, args):
        """takes no arguments

        For some testings.
        """

        capability='admin'
        if not ircdb.checkCapability(msg.prefix, capability):
            irc.errorNoCapability(capability, Raise=True)
        else:
            irc.reply('yeah you are admin')
    test = wrap(test)
	
	def status(self, irc, msg, args, toSet, password):
		"""[<open|close><password>]
		
		open or close fNordeingang.
		"""
		
		
	status = wrap(status)

Class = fNord


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
